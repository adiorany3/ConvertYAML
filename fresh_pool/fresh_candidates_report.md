# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-85MS` (url=201ms, nekobox=228ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-100MS` (url=221ms, nekobox=237ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-103MS` (url=219ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-136MS` (url=232ms, nekobox=250ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-149MS` (url=199ms, nekobox=201ms, status=no)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=238ms, nekobox=194ms, status=no)
7. `AKUN-005-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-150MS`
8. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS`
9. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-68MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-86MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-272MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-287MS` (url=4538ms, nekobox=423ms, status=no)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-299MS` (url=2490ms, nekobox=405ms, status=no)
14. `AKUN-010-CLOUDFLARE-VLESS-WS-291MS`
15. `AKUN-017-CLOUDFLARE-VLESS-WS-304MS` (url=597ms, status=HTTP 204)
16. `AKUN-022-CLOUDFLARE-VLESS-WS-385MS` (url=631ms, status=HTTP 204)
17. `AKUN-023-CLOUDFLARE-VLESS-WS-458MS` (url=712ms, status=HTTP 204)
18. `AKUN-024-CLOUDFLARE-VLESS-WS-407MS` (url=675ms, status=HTTP 204)
19. `AKUN-027-DEV-VLESS-WS-468MS` (url=640ms, status=HTTP 204)
20. `AKUN-032-CLOUDFLARE-VLESS-WS-622MS` (url=985ms, status=HTTP 204)
21. `AKUN-034-JISON-VLESS-WS-368MS` (url=639ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
