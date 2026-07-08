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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=203ms, nekobox=237ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-68MS` (url=211ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=221ms, nekobox=246ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=207ms, nekobox=238ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=204ms, nekobox=236ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-74MS` (url=224ms, nekobox=232ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-89MS` (url=217ms, nekobox=236ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS` (url=217ms, nekobox=259ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-112MS` (url=229ms, nekobox=260ms, status=yes)
10. `AKUN-010-WPENG-VLESS-WS-90MS` (url=215ms, nekobox=236ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-91MS` (url=203ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-114MS` (url=226ms, status=HTTP 204)
13. `AKUN-013-U1HOST-FRA-VLESS-WS-77MS` (url=221ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-82MS` (url=238ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-106MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-81MS` (url=216ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-70MS` (url=232ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-187MS` (url=424ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-116MS` (url=224ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-85MS` (url=232ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-224MS` (url=508ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-250MS` (url=550ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-229MS` (url=498ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-248MS` (url=477ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-260MS` (url=575ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
