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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=210ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=201ms, nekobox=252ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-74MS` (url=217ms, nekobox=7177ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS`
9. `AKUN-008-DIXONS-VLESS-WS-70MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-79MS`
11. `AKUN-010-1PASSWORD-VLESS-WS-77MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-75MS` (url=228ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-83MS` (url=211ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-91MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-72MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-80MS` (url=207ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-82MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-90MS` (url=210ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-93MS` (url=213ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-106MS` (url=222ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-89MS` (url=359ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-79MS` (url=217ms, status=HTTP 204)
23. `AKUN-023-466688-VLESS-WS-95MS` (url=216ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-95MS` (url=213ms, status=HTTP 204)
25. `AKUN-025-MEDIUM-VLESS-WS-73MS` (url=205ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
