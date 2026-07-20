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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=231ms, nekobox=263ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-65MS` (url=222ms, nekobox=278ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-93MS` (url=232ms, nekobox=262ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-79MS` (url=243ms, nekobox=314ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS` (url=264ms, nekobox=294ms, status=yes)
6. `AKUN-006-GO-DADDY-COM-LLC-VLESS-WS-74MS` (url=262ms, nekobox=280ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-74MS` (url=235ms, nekobox=256ms, status=yes)
8. `AKUN-008-ZVC-VLESS-WS-100MS` (url=256ms, nekobox=267ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=252ms, nekobox=291ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-76MS` (url=227ms, nekobox=260ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-86MS` (url=268ms, status=HTTP 204)
12. `AKUN-012-UK-GB-DCL-01-20191003-VLESS-WS-98MS` (url=260ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-133MS` (url=281ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-117MS` (url=281ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-138MS` (url=320ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-97MS` (url=241ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-77MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-UK-GB-DCL-01-20191003-VLESS-WS-126MS` (url=264ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-94MS` (url=256ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-155MS` (url=297ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-160MS` (url=233ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-186MS` (url=330ms, status=HTTP 204)
23. `AKUN-023-WPENG-VLESS-WS-87MS` (url=256ms, status=HTTP 204)
24. `AKUN-024-ZOOM-VLESS-WS-88MS` (url=313ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-123MS` (url=316ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
