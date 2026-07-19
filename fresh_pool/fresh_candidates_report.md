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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-RU-BEGET-20090529-VLESS-WS-61MS` (url=198ms, nekobox=226ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-61MS` (url=201ms, nekobox=224ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-65MS` (url=196ms, nekobox=230ms, status=yes)
4. `AKUN-004-102-177-176-0-102-177-17-VLESS-WS-66MS` (url=208ms, nekobox=241ms, status=yes)
5. `AKUN-005-INTERNETWORKS-45-131-6-0-VLESS-WS-66MS` (url=208ms, nekobox=238ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=214ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-71MS` (url=208ms, nekobox=240ms, status=yes)
8. `AKUN-008-DEV-VLESS-WS-74MS` (url=207ms, nekobox=235ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-84MS` (url=204ms, nekobox=260ms, status=yes)
10. `AKUN-010-CCWU-VLESS-WS-68MS` (url=215ms, nekobox=253ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-80MS` (url=215ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-90MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-92MS` (url=199ms, status=HTTP 204)
15. `AKUN-015-466688-VLESS-WS-82MS` (url=212ms, status=HTTP 204)
16. `AKUN-016-NFORCE-VLESS-WS-78MS` (url=212ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-76MS` (url=219ms, status=HTTP 204)
18. `AKUN-018-ZVC-VLESS-WS-89MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-GO-DADDY-COM-LLC-VLESS-WS-98MS` (url=212ms, status=HTTP 204)
20. `AKUN-020-UK-GB-DCL-01-20191003-VLESS-WS-105MS` (url=207ms, status=HTTP 204)
21. `AKUN-021-WEBEX-VLESS-WS-106MS` (url=215ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-103MS` (url=217ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-111MS` (url=216ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-111MS` (url=252ms, status=HTTP 204)
25. `AKUN-025-US-VLESS-WS-117MS` (url=214ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
