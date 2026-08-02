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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=202ms, nekobox=223ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-62MS` (url=196ms, nekobox=225ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-58MS` (url=196ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-79MS` (url=212ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=200ms, nekobox=230ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS` (url=206ms, nekobox=238ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-93MS` (url=199ms, nekobox=250ms, status=yes)
8. `AKUN-008-FASTVPSUS-IPV4-VLESS-WS-103MS` (url=218ms, nekobox=492ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-62MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-116MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-133MS` (url=331ms, status=HTTP 204)
12. `AKUN-015-SUKARIO-VLESS-WS-392MS` (url=871ms, status=HTTP 204)
13. `AKUN-017-UNKNOWN-VLESS-WS-388MS` (url=646ms, status=HTTP 204)
14. `AKUN-018-CLOUDFLARE-VLESS-WS-424MS` (url=810ms, status=HTTP 204)
15. `AKUN-019-CLOUDFLARE-VLESS-WS-399MS` (url=686ms, status=HTTP 204)
16. `AKUN-020-UNKNOWN-VLESS-WS-422MS` (url=795ms, status=HTTP 204)
17. `AKUN-022-UNKNOWN-VLESS-WS-414MS` (url=682ms, status=HTTP 204)
18. `AKUN-023-UNKNOWN-VLESS-WS-450MS` (url=726ms, status=HTTP 204)
19. `AKUN-024-UNKNOWN-VLESS-WS-390MS` (url=1206ms, status=HTTP 204)
20. `AKUN-025-UNKNOWN-VLESS-WS-509MS` (url=841ms, status=HTTP 204)
21. `AKUN-027-UNKNOWN-VLESS-WS-483MS` (url=1074ms, status=HTTP 204)
22. `AKUN-028-CLOUDFLARE-VLESS-WS-414MS` (url=736ms, status=HTTP 204)
23. `AKUN-031-CLOUDFLARE-VLESS-WS-690MS` (url=2551ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-398MS` (url=452ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-548MS` (url=818ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
