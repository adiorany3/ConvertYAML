# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-090227-VLESS-WS-81MS` (url=230ms, nekobox=254ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS` (url=205ms, nekobox=262ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-101MS` (url=210ms, nekobox=234ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-95MS` (url=219ms, nekobox=274ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-105MS` (url=214ms, nekobox=242ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-91MS` (url=223ms, nekobox=253ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-100MS` (url=254ms, nekobox=242ms, status=yes)
8. `AKUN-008-DEV-VLESS-WS-130MS` (url=200ms, nekobox=195ms, status=no)
9. `AKUN-009-UNKNOWN-VLESS-WS-245MS` (url=1960ms, nekobox=418ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-288MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-279MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-269MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-279MS` (url=605ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-313MS` (url=2675ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-301MS` (url=596ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-383MS` (url=675ms, status=HTTP 204)
17. `AKUN-020-UNKNOWN-VLESS-WS-204MS` (url=224ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-383MS` (url=730ms, status=HTTP 204)
19. `AKUN-025-CLOUDFLARE-VLESS-WS-470MS` (url=710ms, status=HTTP 204)
20. `AKUN-028-UNKNOWN-VLESS-WS-458MS` (url=842ms, status=HTTP 204)
21. `AKUN-032-RS-RAPIDSEEDBOX-20190717-VLESS-WS-500MS` (url=933ms, status=HTTP 204)
22. `AKUN-035-UNKNOWN-VLESS-WS-97MS` (url=239ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
