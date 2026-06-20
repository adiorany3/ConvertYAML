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
1. `AKUN-001-9889888-VLESS-WS-69MS` (url=233ms, nekobox=260ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-84MS` (url=238ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=242ms, nekobox=270ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-61MS` (url=245ms, nekobox=308ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-82MS` (url=249ms, nekobox=262ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-80MS` (url=225ms, nekobox=256ms, status=yes)
7. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-140MS` (url=239ms, nekobox=260ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=230ms, nekobox=266ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-295MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-283MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-301MS` (url=631ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-268MS` (url=574ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-111MS` (url=307ms, status=HTTP 204)
14. `AKUN-015-YGDFW-VLESS-WS-435MS` (url=746ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-171MS` (url=713ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-461MS` (url=641ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-166MS` (url=687ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-435MS` (url=681ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-476MS` (url=704ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-435MS` (url=687ms, status=HTTP 204)
21. `AKUN-025-BROADNNET-KR-VLESS-WS-505MS` (url=763ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-271MS` (url=568ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-459MS` (url=679ms, status=HTTP 204)
24. `AKUN-031-CLOUDFLARE-VLESS-WS-312MS` (url=637ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-598MS` (url=956ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
