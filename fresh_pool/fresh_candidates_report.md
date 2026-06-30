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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=213ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=215ms, nekobox=243ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-68MS` (url=207ms, nekobox=242ms, status=yes)
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-66MS` (url=239ms, nekobox=254ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=206ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=211ms, nekobox=238ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-105MS` (url=215ms, nekobox=239ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-105MS` (url=214ms, nekobox=230ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-107MS` (url=226ms, nekobox=246ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-102MS` (url=214ms, nekobox=243ms, status=yes)
11. `AKUN-011-MYBB-VLESS-WS-78MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-109MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-110MS` (url=202ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-128MS` (url=217ms, status=HTTP 204)
15. `AKUN-015-COMPREND-NET-VLESS-WS-96MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-74MS` (url=218ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-101MS` (url=212ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-140MS` (url=212ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-73MS` (url=226ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-228MS` (url=537ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-232MS` (url=502ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-268MS` (url=560ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-171MS` (url=591ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-265MS` (url=543ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-255MS` (url=493ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
