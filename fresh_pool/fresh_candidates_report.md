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
1. `AKUN-001-104-253-175-0-1-VLESS-WS-66MS` (url=227ms, nekobox=267ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=222ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-70MS` (url=224ms, nekobox=264ms, status=yes)
4. `AKUN-004-466688-VLESS-WS-72MS` (url=234ms, nekobox=282ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-65MS` (url=231ms, nekobox=266ms, status=yes)
6. `AKUN-006-NODEHOST-VLESS-WS-74MS` (url=249ms, nekobox=271ms, status=yes)
7. `AKUN-007-TENCENT-VLESS-WS-78MS` (url=233ms, nekobox=270ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-104MS` (url=231ms, nekobox=266ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=240ms, nekobox=256ms, status=yes)
10. `AKUN-010-PAGES-VLESS-WS-112MS` (url=246ms, nekobox=278ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-86MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-146MS` (url=347ms, status=HTTP 204)
13. `AKUN-013-ES-FORNEX-20160629-VLESS-WS-131MS` (url=245ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-151MS` (url=237ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-72MS` (url=274ms, status=HTTP 204)
16. `AKUN-016-SPEEDTEST-VLESS-WS-90MS` (url=246ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-115MS` (url=250ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-90MS` (url=246ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-202MS` (url=281ms, status=HTTP 204)
20. `AKUN-020-LT-LRTC-20060503-VLESS-WS-257MS` (url=589ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-273MS` (url=589ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-272MS` (url=544ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-197MS` (url=439ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-259MS` (url=363ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-92MS` (url=247ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
