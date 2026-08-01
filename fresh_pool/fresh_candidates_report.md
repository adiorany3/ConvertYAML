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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-81MS` (url=316ms, nekobox=196ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-85MS`
3. `AKUN-002-UNKNOWN-VLESS-WS-84MS`
4. `AKUN-004-CLOUDFLARE-VLESS-WS-90MS` (url=370ms, nekobox=204ms, status=no)
5. `AKUN-003-MVPS-NET-VLESS-WS-95MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-82MS`
7. `AKUN-005-CLOUDFLARE-VLESS-WS-91MS`
8. `AKUN-006-EU-VLESS-WS-118MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-93MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-137MS` (url=364ms, nekobox=183ms, status=no)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-141MS` (url=283ms, nekobox=182ms, status=no)
13. `AKUN-009-CLOUDFLARE-VLESS-WS-135MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-123MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-133MS` (url=306ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-114MS` (url=317ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-123MS` (url=291ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-135MS` (url=282ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-143MS` (url=318ms, status=HTTP 204)
20. `AKUN-020-RMGYVPN-VLESS-WS-154MS` (url=375ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-160MS` (url=361ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-165MS` (url=412ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-135MS` (url=437ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-211MS` (url=379ms, status=HTTP 204)
25. `AKUN-025-LEVIKOGJGFDD-VLESS-WS-279MS` (url=582ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
