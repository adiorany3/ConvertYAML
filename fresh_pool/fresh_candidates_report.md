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
1. `AKUN-001-UNKNOWN-VLESS-WS-57MS` (url=205ms, nekobox=223ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=199ms, nekobox=223ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-61MS` (url=224ms, nekobox=224ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-62MS` (url=201ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=225ms, nekobox=249ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-98MS` (url=206ms, nekobox=262ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=206ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-68MS` (url=205ms, nekobox=245ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-119MS` (url=207ms, nekobox=232ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-122MS` (url=340ms, nekobox=355ms, status=yes)
11. `AKUN-011-EU-VLESS-WS-91MS` (url=200ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-125MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-85MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-118MS` (url=215ms, status=HTTP 204)
15. `AKUN-015-SPEEDTEST-VLESS-WS-76MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-FASTVPSUS-IPV4-VLESS-WS-85MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-103MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-56MS` (url=198ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-270MS` (url=2725ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-392MS` (url=665ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-404MS` (url=688ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-396MS` (url=650ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-419MS` (url=680ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-418MS` (url=709ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-396MS` (url=703ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
