# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2020 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Attributes that the jsonschema from the Snap Store originally require but
# Snapcraft does not have been commented out from this schema originally
# imported from
# https://dashboard.snapcraft.io/docs/v2/en/snaps.html#snap-channel-map

from typing import Any, Dict

CHANNEL_MAP_JSONSCHEMA: Dict[str, Any] = {
    "additionalProperties": False,
    "properties": {
        "channel-map": {
            "items": {
                "additionalProperties": False,
                "properties": {
                    "architecture": {"type": "string"},
                    "channel": {
                        "description": 'The channel name, including "latest/" for the latest track.',
                        "type": "string",
                    },
                    "expiration-date": {
                        "description": "The date when this release expires, in RFC 3339 format. If null, the release does not expire.",
                        "format": "date-time",
                        "type": ["string", "null"],
                    },
                    "progressive": {
                        "additionalProperties": False,
                        "properties": {
                            "key": {"type": ["string", "null"]},
                            "paused": {"type": ["boolean", "null"]},
                            "percentage": {"type": ["number", "null"]},
                        },
                        "required": ["key", "paused", "percentage"],
                        "type": "object",
                    },
                    "revision": {"type": "integer"},
                    "when": {
                        "description": "The date when this release was made, in RFC 3339 format.",
                        "format": "date-time",
                        "type": "string",
                    },
                },
                "required": [
                    "architecture",
                    "channel",
                    "expiration-date",
                    "progressive",
                    "revision",
                    # "when"
                ],
                "type": "object",
            },
            "minItems": 0,
            "type": "array",
        },
        "revisions": {
            "items": {
                "additionalProperties": False,
                "properties": {
                    "architectures": {
                        "items": {"type": "string"},
                        "minItems": 1,
                        "type": "array",
                    },
                    "attributes": {"type": "object"},
                    "base": {"type": ["string", "null"]},
                    "build-url": {"type": ["string", "null"]},
                    "confinement": {
                        "enum": ["strict", "classic", "devmode"],
                        "type": "string",
                    },
                    "created-at": {"format": "date-time", "type": "string"},
                    "epoch": {
                        "additionalProperties": False,
                        "properties": {
                            "read": {
                                "items": {"type": "integer"},
                                "minItems": 1,
                                "type": ["array", "null"],
                            },
                            "write": {
                                "items": {"type": "integer"},
                                "minItems": 1,
                                "type": ["array", "null"],
                            },
                        },
                        "required": ["read", "write"],
                        "type": "object",
                    },
                    "grade": {"enum": ["stable", "devel"], "type": "string"},
                    "revision": {"type": "integer"},
                    "sha3-384": {"type": "string"},
                    "size": {"type": "integer"},
                    "version": {"type": "string"},
                },
                "required": [
                    "architectures",
                    # "attributes",
                    # "base",
                    # "build-url",
                    # "confinement",
                    # "created-at",
                    # "epoch",
                    # "grade",
                    "revision",
                    # "sha3-384",
                    # "size",
                    # "status",
                    "version",
                ],
                "type": "object",
            },
            "minItems": 0,
            "type": "array",
        },
        "snap": {
            "additionalProperties": False,
            "description": "Metadata about the requested snap.",
            "introduced_at": 6,
            "properties": {
                "channels": {
                    "description": "The list of most relevant channels for this snap. Branches are only included if there is a release for it.",
                    "introduced_at": 9,
                    "items": {
                        "additionalProperties": False,
                        "description": "A list of channels and their metadata for the requested snap.",
                        "properties": {
                            "branch": {
                                "description": "The branch name for this channel, can be null.",
                                "type": ["string", "null"],
                            },
                            "fallback": {
                                "description": "The name of the channel that this channel would fall back to if there were no releases in it. If null, this channel has no fallback channel.",
                                "type": ["string", "null"],
                            },
                            "name": {
                                "description": 'The channel name, including "latest/" for the latest track.',
                                "type": "string",
                            },
                            "risk": {
                                "description": "The risk name for this channel.",
                                "type": "string",
                            },
                            "track": {
                                "description": "The track name for this channel.",
                                "type": "string",
                            },
                        },
                        "required": ["name", "track", "risk", "branch", "fallback"],
                        "type": "object",
                    },
                    "minItems": 1,
                    "type": "array",
                },
                "default-track": {
                    "description": "The default track name for this snap. If no default track is set, this value is null.",
                    "type": ["string", "null"],
                },
                "id": {
                    "description": "The snap ID for this snap package.",
                    "type": "string",
                },
                "name": {"description": "The snap package name.", "type": "string"},
                "private": {
                    "description": "Whether this snap is private or not.",
                    "type": "boolean",
                },
                "tracks": {
                    "description": "An ordered list of most relevant tracks for this snap.",
                    "introduced_at": 9,
                    "items": {
                        "additionalProperties": False,
                        "description": "An ordered list of tracks and their metadata for this snap.",
                        "properties": {
                            "creation-date": {
                                "description": "The track creation date, in ISO 8601 format.",
                                "format": "date-time",
                                "type": ["string", "null"],
                            },
                            "name": {
                                "description": "The track name.",
                                "type": "string",
                            },
                            "version-pattern": {
                                "description": "A Python regex to validate the versions being released to this track. If null, no validation is enforced.",
                                "type": ["string", "null"],
                            },
                        },
                        # pattern is documented as required but is not returned,
                        # version-pattern is returned instead.
                        "required": ["name", "creation-date", "version-pattern"],
                        "type": "object",
                    },
                    "minItems": 1,
                    "type": "array",
                },
            },
            "required": [
                # "id",
                "channels",
                # "default-track",
                "name",
                # "private",
                # "tracks"
            ],
            "type": "object",
        },
    },
    "required": ["channel-map", "revisions", "snap"],
    "type": "object",
}
