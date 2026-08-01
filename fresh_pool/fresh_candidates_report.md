# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-UNKNOWN-VLESS-WS-85MS` (url=200ms, nekobox=231ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-84MS` (url=217ms, nekobox=245ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-89MS` (url=198ms, nekobox=227ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-90MS` (url=230ms, nekobox=261ms, status=yes)
5. `AKUN-005-LEVIKOGJGFDD-VLESS-WS-92MS` (url=202ms, nekobox=237ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=199ms, nekobox=231ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS` (url=229ms, nekobox=225ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-91MS` (url=202ms, nekobox=228ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-104MS` (url=224ms, nekobox=242ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-106MS` (url=207ms, nekobox=232ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-146MS` (url=310ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-125MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-147MS` (url=382ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-158MS` (url=345ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-173MS` (url=360ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-141MS` (url=272ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-300MS` (url=627ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-359MS` (url=1159ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-548MS` (url=5728ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-614MS` (url=998ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-627MS` (url=972ms, status=HTTP 204)
22. `AKUN-025-UNKNOWN-VLESS-WS-648MS` (url=1119ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-676MS` (url=1314ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-675MS` (url=1325ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-689MS` (url=1130ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
