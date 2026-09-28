# Version and Update Policy

GitHub `manifest.json` on the stable branch is the canonical version manifest.

## Channels
- stable: recommended for normal use.
- future prerelease channels may be added explicitly; never assume them.

## Platform behavior

### Gemini
Knowledge files may be linked from Google Drive. The Gem should treat the Drive copy of `PURCHASE-RESEARCH.md` and `VERSION.json` as operational truth. At the beginning of a substantial new research project, it may compare the local Knowledge version with the public stable manifest. If GitHub is newer, inform the user and propose updating the Drive Knowledge files. Do not claim to edit the Gem's own instructions unless that capability is actually available.

### Hermes
Compare local skill version to stable manifest when explicitly asked to check updates or when starting maintenance of the skill. Never self-update silently. Present the version difference/changelog and require explicit authorization before replacing skill files.

### ChatGPT / other skill hosts
If update checking is possible, compare installed metadata.version to the stable manifest and offer the update. Do not assume the host supports self-update.

### ChatGPT Free
The prompt cannot reliably self-replace. It may point the user to the stable manifest/repository when update checking is requested.

## Rule
Update notification is allowed; automatic mutation requires platform capability plus explicit user authorization.
