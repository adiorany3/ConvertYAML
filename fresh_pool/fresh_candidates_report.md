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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-58MS` (url=219ms, nekobox=233ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-58MS` (url=223ms, nekobox=246ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=213ms, nekobox=251ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=220ms, nekobox=253ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-63MS` (url=217ms, nekobox=300ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-74MS` (url=192ms, nekobox=259ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-68MS` (url=217ms, nekobox=244ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-89MS` (url=208ms, nekobox=251ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=216ms, nekobox=233ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-68MS` (url=205ms, nekobox=252ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-132MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-107MS` (url=195ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-88MS` (url=222ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-109MS` (url=230ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-120MS` (url=213ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-127MS` (url=219ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-147MS` (url=212ms, status=HTTP 204)
18. `AKUN-019-090227-VLESS-WS-319MS` (url=640ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-347MS` (url=2761ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-407MS` (url=4896ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-594MS` (url=955ms, status=HTTP 204)
22. `AKUN-024-SUKARIO-VLESS-WS-670MS` (url=1087ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-678MS` (url=1087ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-694MS` (url=2270ms, status=HTTP 204)
25. `AKUN-031-UNKNOWN-VLESS-WS-746MS` (url=1184ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
