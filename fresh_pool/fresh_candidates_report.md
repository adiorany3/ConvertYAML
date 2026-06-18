# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-UNKNOWN-VLESS-WS-94MS` (url=232ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-87MS` (url=208ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=224ms, nekobox=234ms, status=yes)
4. `AKUN-004-DEV-VLESS-WS-110MS` (url=226ms, nekobox=187ms, status=no)
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS`
6. `AKUN-005-VULTR-VLESS-WS-80MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS`
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-112MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS` (url=218ms, nekobox=212ms, status=no)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-140MS` (url=212ms, nekobox=177ms, status=no)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-101MS` (url=217ms, nekobox=196ms, status=no)
13. `AKUN-009-CLOUDFLARE-VLESS-WS-370MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-391MS`
15. `AKUN-015-CLOUDFLARE-VLESS-WS-391MS` (url=2795ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-401MS` (url=815ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-409MS` (url=2923ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-402MS` (url=858ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-272MS` (url=917ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-520MS` (url=899ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-642MS` (url=1029ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-686MS` (url=1161ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-761MS` (url=1190ms, status=HTTP 204)
24. `AKUN-033-CLOUDFLARE-VLESS-WS-787MS` (url=4190ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
