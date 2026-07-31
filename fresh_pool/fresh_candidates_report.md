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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=215ms, nekobox=244ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=226ms, nekobox=244ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=216ms, nekobox=247ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-78MS` (url=214ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-77MS` (url=222ms, nekobox=246ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-80MS` (url=216ms, nekobox=249ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=213ms, nekobox=249ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-86MS` (url=207ms, nekobox=257ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-84MS` (url=226ms, nekobox=246ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-87MS` (url=233ms, nekobox=243ms, status=yes)
11. `AKUN-011-RMGYVPN-VLESS-WS-140MS` (url=351ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-105MS` (url=400ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-142MS` (url=231ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-250MS` (url=3828ms, status=HTTP 204)
15. `AKUN-018-NOTION-WEB-VLESS-WS-282MS` (url=719ms, status=HTTP 204)
16. `AKUN-019-CN-CF-VLESS-WS-301MS` (url=629ms, status=HTTP 204)
17. `AKUN-021-CLOUDFLARE-VLESS-WS-398MS` (url=703ms, status=HTTP 204)
18. `AKUN-022-CLOUDFLARE-VLESS-WS-414MS` (url=745ms, status=HTTP 204)
19. `AKUN-025-CLOUDFLARE-VLESS-WS-512MS` (url=1174ms, status=HTTP 204)
20. `AKUN-027-CLOUDFLARE-VLESS-WS-427MS` (url=670ms, status=HTTP 204)
21. `AKUN-029-CLOUDFLARE-VLESS-WS-468MS` (url=1443ms, status=HTTP 204)
22. `AKUN-031-CLOUDFLARE-VLESS-WS-527MS` (url=862ms, status=HTTP 204)
23. `AKUN-032-UNKNOWN-VLESS-WS-554MS` (url=1192ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-643MS` (url=1261ms, status=HTTP 204)
25. `AKUN-034-CLOUDFLARE-VLESS-WS-666MS` (url=1305ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
