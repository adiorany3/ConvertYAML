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
1. `AKUN-001-UNKNOWN-VLESS-WS-86MS` (url=254ms, nekobox=296ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=254ms, nekobox=313ms, status=yes)
3. `AKUN-003-ICOOK-VLESS-WS-105MS` (url=271ms, nekobox=337ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-110MS` (url=299ms, nekobox=340ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-116MS` (url=341ms, nekobox=276ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS` (url=279ms, nekobox=325ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-105MS` (url=253ms, nekobox=300ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-143MS` (url=262ms, nekobox=341ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-127MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-141MS`
11. `AKUN-012-UNKNOWN-VLESS-WS-113MS` (url=266ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-125MS` (url=247ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-127MS` (url=298ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-188MS` (url=372ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-196MS` (url=345ms, status=HTTP 204)
16. `AKUN-017-090227-VLESS-WS-176MS` (url=386ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-213MS` (url=409ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-158MS` (url=349ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-228MS` (url=394ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-215MS` (url=399ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-206MS` (url=350ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-569MS` (url=986ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-616MS` (url=1054ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-546MS` (url=1150ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-643MS` (url=4200ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
