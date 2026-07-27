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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=219ms, nekobox=251ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-78MS` (url=199ms, nekobox=260ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=215ms, nekobox=247ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-83MS` (url=221ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-85MS` (url=217ms, nekobox=244ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=214ms, nekobox=262ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-86MS` (url=217ms, nekobox=252ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-79MS` (url=212ms, nekobox=240ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-94MS` (url=214ms, nekobox=247ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-101MS` (url=214ms, nekobox=255ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-97MS` (url=236ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-99MS` (url=221ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-77MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-109MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-EU-VLESS-WS-98MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-134MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-102MS` (url=209ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-117MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-149MS` (url=218ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-158MS` (url=260ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-124MS` (url=266ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-232MS` (url=5158ms, status=HTTP 204)
24. `AKUN-024-NET-141-11-202-0-23-VLESS-WS-248MS` (url=510ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-414MS` (url=691ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
