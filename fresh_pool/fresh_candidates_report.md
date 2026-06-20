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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=197ms, nekobox=169ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS`
3. `AKUN-002-UNKNOWN-VLESS-WS-71MS`
4. `AKUN-003-090227-VLESS-WS-79MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS`
6. `AKUN-005-UNKNOWN-VLESS-WS-76MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-82MS`
8. `AKUN-009-CLOUDFLARE-VLESS-WS-90MS` (url=199ms, nekobox=184ms, status=no)
9. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-89MS`
10. `AKUN-011-UNKNOWN-VLESS-WS-90MS` (url=194ms, nekobox=182ms, status=no)
11. `AKUN-008-CLOUDFLARE-VLESS-WS-71MS`
12. `AKUN-009-CLOUDFLARE-VLESS-WS-399MS`
13. `AKUN-010-CLOUDFLARE-VLESS-WS-360MS`
14. `AKUN-016-UNKNOWN-VLESS-WS-394MS` (url=867ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-418MS` (url=847ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-68MS` (url=221ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-405MS` (url=811ms, status=HTTP 204)
18. `AKUN-022-JISON-VLESS-WS-561MS` (url=1077ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-627MS` (url=840ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-642MS` (url=893ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-654MS` (url=874ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-663MS` (url=925ms, status=HTTP 204)
23. `AKUN-029-BROADNNET-KR-VLESS-WS-652MS` (url=795ms, status=HTTP 204)
24. `AKUN-035-RS-RAPIDSEEDBOX-20190717-VLESS-WS-751MS` (url=1244ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
