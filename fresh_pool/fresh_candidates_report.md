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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-136MS` (url=272ms, nekobox=298ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-141MS` (url=247ms, nekobox=235ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-139MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-143MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-140MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-140MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-151MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-151MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-141MS` (url=244ms, nekobox=294ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-140MS`
11. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-154MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-152MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-153MS` (url=282ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-142MS` (url=296ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-147MS` (url=272ms, status=HTTP 204)
16. `AKUN-016-IDC-SG-VLESS-WS-159MS` (url=282ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-167MS` (url=283ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-177MS` (url=300ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-150MS` (url=271ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-152MS` (url=303ms, status=HTTP 204)
21. `AKUN-021-PAGES-VLESS-WS-179MS` (url=342ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-168MS` (url=278ms, status=HTTP 204)
23. `AKUN-023-WEBEX-VLESS-WS-145MS` (url=288ms, status=HTTP 204)
24. `AKUN-024-3666888-VLESS-WS-172MS` (url=322ms, status=HTTP 204)
25. `AKUN-025-POLICE-VLESS-WS-153MS` (url=315ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
