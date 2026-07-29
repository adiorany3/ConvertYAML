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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=209ms, nekobox=227ms, status=yes)
2. `AKUN-002-HOSTINGER-VLESS-WS-63MS` (url=203ms, nekobox=228ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-65MS` (url=212ms, nekobox=233ms, status=yes)
4. `AKUN-004-SEECK-VLESS-WS-61MS` (url=207ms, nekobox=224ms, status=yes)
5. `AKUN-005-ICOOK-VLESS-WS-86MS` (url=225ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=222ms, nekobox=239ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=201ms, nekobox=186ms, status=no)
8. `AKUN-007-ZVC-VLESS-WS-72MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-74MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-110MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-82MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-64MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-FMN5-RENTED-NET2-VLESS-WS-96MS` (url=222ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-99MS` (url=201ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-100MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-140MS` (url=212ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-125MS` (url=321ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-142MS` (url=247ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-79MS` (url=207ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-84MS` (url=236ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-195MS` (url=247ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-206MS` (url=213ms, status=HTTP 204)
23. `AKUN-024-CONFLU-VLESS-WS-226MS` (url=479ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-274MS` (url=5107ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-400MS` (url=641ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
