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
1. `AKUN-001-UNKNOWN-VLESS-WS-67MS` (url=207ms, nekobox=237ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=201ms, nekobox=230ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=213ms, nekobox=239ms, status=yes)
4. `AKUN-004-ORG-VLESS-WS-76MS` (url=220ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=217ms, nekobox=230ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS` (url=208ms, nekobox=240ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=220ms, nekobox=256ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=221ms, nekobox=231ms, status=yes)
9. `AKUN-009-ZVC-VLESS-WS-77MS` (url=209ms, nekobox=227ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-79MS` (url=214ms, nekobox=245ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-102MS` (url=244ms, status=HTTP 204)
12. `AKUN-012-CZ-LOTUNA-19970206-VLESS-WS-69MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-111MS` (url=214ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-81MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-97MS` (url=200ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-92MS` (url=205ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-103MS` (url=205ms, status=HTTP 204)
18. `AKUN-018-UK-GB-DCL-01-20191003-VLESS-WS-107MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-115MS` (url=219ms, status=HTTP 204)
20. `AKUN-020-ZVC-VLESS-WS-107MS` (url=209ms, status=HTTP 204)
21. `AKUN-021-UK-GB-DCL-01-20191003-VLESS-WS-132MS` (url=213ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-130MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-110MS` (url=215ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-235MS` (url=1204ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-264MS` (url=531ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
