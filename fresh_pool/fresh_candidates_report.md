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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=201ms, nekobox=230ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-67MS` (url=198ms, nekobox=240ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=223ms, nekobox=236ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-69MS` (url=199ms, nekobox=185ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-75MS` (url=201ms, nekobox=183ms, status=no)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=196ms, nekobox=200ms, status=no)
7. `AKUN-004-UNKNOWN-VLESS-WS-80MS`
8. `AKUN-005-WEYRO-NET-VLESS-WS-76MS`
9. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-95MS` (url=230ms, nekobox=189ms, status=no)
11. `AKUN-007-CLOUDFLARE-VLESS-WS-68MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-92MS`
13. `AKUN-009-ADF-VLESS-WS-82MS`
14. `AKUN-010-UNKNOWN-VLESS-WS-77MS`
15. `AKUN-015-UNKNOWN-VLESS-WS-100MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-SSL-1134-VLESS-WS-93MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-81MS` (url=214ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-86MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-WPENG-VLESS-WS-70MS` (url=215ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-102MS` (url=215ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-72MS` (url=207ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-249MS` (url=538ms, status=HTTP 204)
23. `AKUN-023-TANG-NET-VLESS-WS-252MS` (url=529ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-263MS` (url=541ms, status=HTTP 204)
25. `AKUN-025-WPENG-VLESS-WS-294MS` (url=545ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
