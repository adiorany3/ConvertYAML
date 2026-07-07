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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=234ms, nekobox=239ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-64MS` (url=223ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=234ms, nekobox=181ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-59MS`
7. `AKUN-006-WPENG-VLESS-WS-60MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-68MS` (url=242ms, nekobox=178ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-70MS` (url=236ms, nekobox=177ms, status=no)
11. `AKUN-008-WPENG-VLESS-WS-62MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS`
14. `AKUN-014-DEV-VLESS-WS-87MS` (url=253ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-122MS` (url=219ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-103MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-76MS` (url=233ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-75MS` (url=218ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-97MS` (url=227ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-342MS` (url=750ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-373MS` (url=781ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-392MS` (url=839ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-402MS` (url=921ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-400MS` (url=854ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-84MS` (url=232ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
