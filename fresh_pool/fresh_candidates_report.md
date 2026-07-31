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
1. `AKUN-001-UNKNOWN-VLESS-WS-58MS` (url=201ms, nekobox=223ms, status=yes)
2. `AKUN-002-ICOOK-VLESS-WS-61MS` (url=202ms, nekobox=244ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-58MS` (url=221ms, nekobox=243ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-60MS` (url=211ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS` (url=199ms, nekobox=223ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-70MS` (url=225ms, nekobox=238ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-98MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-121MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-127MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-172MS`
11. `AKUN-012-090227-VLESS-WS-158MS` (url=330ms, status=HTTP 204)
12. `AKUN-013-NET-141-11-202-0-23-VLESS-WS-224MS` (url=482ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-257MS` (url=504ms, status=HTTP 204)
14. `AKUN-018-CLOUDFLARE-VLESS-WS-406MS` (url=716ms, status=HTTP 204)
15. `AKUN-019-UNKNOWN-VLESS-WS-258MS` (url=270ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-445MS` (url=891ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-438MS` (url=781ms, status=HTTP 204)
18. `AKUN-022-UNKNOWN-VLESS-WS-450MS` (url=733ms, status=HTTP 204)
19. `AKUN-023-UNKNOWN-VLESS-WS-455MS` (url=778ms, status=HTTP 204)
20. `AKUN-025-UNKNOWN-VLESS-WS-391MS` (url=647ms, status=HTTP 204)
21. `AKUN-027-CLOUDFLARE-VLESS-WS-503MS` (url=840ms, status=HTTP 204)
22. `AKUN-030-UNKNOWN-VLESS-WS-548MS` (url=903ms, status=HTTP 204)
23. `AKUN-031-CLOUDFLARE-VLESS-WS-535MS` (url=761ms, status=HTTP 204)
24. `AKUN-032-CLOUDFLARE-VLESS-WS-564MS` (url=1201ms, status=HTTP 204)
25. `AKUN-034-UNKNOWN-VLESS-WS-883MS` (url=1277ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
