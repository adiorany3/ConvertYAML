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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=237ms, nekobox=253ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-73MS` (url=271ms, nekobox=199ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS`
4. `AKUN-003-OVH-VLESS-WS-74MS`
5. `AKUN-004-WPENG-VLESS-WS-71MS`
6. `AKUN-005-INTERNETWORKS-45-131-6-0-VLESS-WS-74MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-83MS` (url=262ms, nekobox=185ms, status=no)
8. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS`
9. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-64MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-75MS`
11. `AKUN-009-WEYRO-NET-VLESS-WS-69MS`
12. `AKUN-010-ZVC-VLESS-WS-84MS`
13. `AKUN-013-UNKNOWN-VLESS-WS-81MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-99MS` (url=222ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-94MS` (url=263ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-91MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-94MS` (url=212ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-73MS` (url=268ms, status=HTTP 204)
19. `AKUN-019-466688-VLESS-WS-121MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-WPENG-VLESS-WS-145MS` (url=239ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-364MS` (url=783ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-368MS` (url=788ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-386MS` (url=851ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-364MS` (url=735ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-391MS` (url=831ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
