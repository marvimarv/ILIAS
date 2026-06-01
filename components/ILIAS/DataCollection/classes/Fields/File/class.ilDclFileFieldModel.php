<?php

/**
 * This file is part of ILIAS, a powerful learning management system
 * published by ILIAS open source e-Learning e.V.
 *
 * ILIAS is licensed with the GPL-3.0,
 * see https://www.gnu.org/licenses/gpl-3.0.en.html
 * You should have received a copy of said license along with the
 * source code, too.
 *
 * If this is not the case or you just want to try ILIAS, you'll find
 * us at:
 * https://www.ilias.de
 * https://github.com/ILIAS-eLearning
 *
 *********************************************************************/

declare(strict_types=1);

/**
 * @noinspection AutoloadingIssuesInspection
 */
class ilDclFileFieldModel extends ilDclBaseFieldModel
{
    protected ilFileServicesSettings $file_settings;

    public function __construct(int $a_id = 0)
    {
        global $DIC;
        $this->file_settings = $DIC->fileServiceSettings();
        parent::__construct($a_id);
    }

    public function allowFilterInListView(): bool
    {
        return false;
    }

    public function getValidFieldProperties(): array
    {
        return [ilDclBaseFieldModel::PROP_SUPPORTED_FILE_TYPES];
    }

    public function getSupportedExtensions(): array
    {
        $file_types = [];

        foreach ($this->getExtensions() as $i => $type) {
            if (
                in_array($type, $this->file_settings->getWhiteListedSuffixes()) &&
                !in_array($type, $this->file_settings->getBlackListedSuffixes())
            ) {
                $file_types[] = $type;
            }
        }

        return $file_types;
    }

    protected function getExtensions(): array
    {
        $types = $this->getProperty(ilDclBaseFieldModel::PROP_SUPPORTED_FILE_TYPES);
        if ($types === null) {
            return [];
        } else {
            return explode(',', str_replace(' ', '', $types));
        }
    }

    public function checkValidityFromForm(ilPropertyFormGUI &$form, ?int $record_id = null): void
    {
        $post_var = 'field_' . $this->getId();
        $upload = $_FILES[$post_var] ?? null;

        if (is_array($upload)
            && isset($upload['name'])
            && is_string($upload['name'])
            && $upload['name'] !== ''
        ) {
            $ascii_name = ilFileUtils::getASCIIFilename($upload['name']);
            $mime = is_string($upload['type'] ?? null) ? $upload['type'] : 'application/octet-stream';

            $overhead = strlen(session_id())
                + 32                                                // md5 ilfilehash
                + strlen($post_var)
                + strlen(str_replace('/', '~~', $mime))
                + (6 * strlen('~~'));                               // six separators in the temp filename
            $safety_margin = 16;
            $max_name_bytes = 255 - $overhead - $safety_margin;

            if ($max_name_bytes > 0 && strlen($ascii_name) > $max_name_bytes) {
                throw new ilDclInputException(
                    ilDclInputException::FILENAME_TOO_LONG,
                    (string) $max_name_bytes
                );
            }
        }

        parent::checkValidityFromForm($form, $record_id);
    }
}
