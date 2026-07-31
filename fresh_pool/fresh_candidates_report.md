# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-236MS` (url=425ms, nekobox=707ms, status=yes)
2. `AKUN-002-ICOOK-VLESS-WS-224MS` (url=1403ms, nekobox=720ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-242MS` (url=630ms, nekobox=948ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-236MS` (url=401ms, nekobox=1046ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-238MS` (url=376ms, nekobox=479ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-236MS` (url=438ms, nekobox=403ms, status=yes)
7. `AKUN-007-RMGYVPN-VLESS-WS-537MS` (url=896ms, nekobox=1303ms, status=yes)
8. `AKUN-008-PAGES-VLESS-WS-239MS` (url=453ms, nekobox=668ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-348MS` (url=1843ms, nekobox=425ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-745MS`
11. `AKUN-013-UNKNOWN-VLESS-WS-815MS` (url=1394ms, status=HTTP 204)
12. `AKUN-015-CLOUDFLARE-VLESS-WS-873MS` (url=1314ms, status=HTTP 204)
13. `AKUN-016-CLOUDFLARE-VLESS-WS-897MS` (url=1323ms, status=HTTP 204)
14. `AKUN-018-CLOUDFLARE-VLESS-WS-885MS` (url=1660ms, status=HTTP 204)
15. `AKUN-019-CLOUDFLARE-VLESS-WS-828MS` (url=2201ms, status=HTTP 204)
16. `AKUN-020-UNKNOWN-VLESS-WS-885MS` (url=1472ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-851MS` (url=1674ms, status=HTTP 204)
18. `AKUN-022-TW-CLOUD-VLESS-WS-814MS` (url=1463ms, status=HTTP 204)
19. `AKUN-023-UNKNOWN-VLESS-WS-244MS` (url=1425ms, status=HTTP 204)
20. `AKUN-024-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-375MS` (url=653ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-837MS` (url=1867ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-838MS` (url=1730ms, status=HTTP 204)
23. `AKUN-027-UNKNOWN-VLESS-WS-836MS` (url=1702ms, status=HTTP 204)
24. `AKUN-031-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-557MS` (url=1953ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
