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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=211ms, nekobox=170ms, status=no)
2. `AKUN-001-UNKNOWN-VLESS-WS-62MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-69MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-60MS` (url=220ms, nekobox=181ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-62MS`
7. `AKUN-005-UNKNOWN-VLESS-WS-61MS`
8. `AKUN-006-UNKNOWN-VLESS-WS-68MS`
9. `AKUN-007-ADF-VLESS-WS-64MS`
10. `AKUN-008-MYBB-VLESS-WS-102MS`
11. `AKUN-009-PAGES-VLESS-WS-99MS`
12. `AKUN-010-DEV-VLESS-WS-62MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-65MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-1PASSWORD-VLESS-WS-91MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-ZVC-VLESS-WS-58MS` (url=209ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-119MS` (url=216ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-73MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-LEVIKOGJGFDD-VLESS-WS-91MS` (url=204ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-68MS` (url=206ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-63MS` (url=198ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-70MS` (url=205ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-81MS` (url=224ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-63MS` (url=202ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-71MS` (url=205ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-69MS` (url=209ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
