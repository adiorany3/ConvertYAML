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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-75MS` (url=217ms, nekobox=227ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS` (url=219ms, nekobox=235ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-85MS` (url=212ms, nekobox=236ms, status=yes)
4. `AKUN-004-PUBLICDOMAINREGISTRY-NET-VLESS-WS-89MS` (url=208ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-103MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS`
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-111MS`
8. `AKUN-008-VULTR-VLESS-WS-103MS`
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-138MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-130MS` (url=222ms, status=HTTP 204)
12. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-101MS` (url=199ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-102MS` (url=259ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-257MS` (url=578ms, status=HTTP 204)
15. `AKUN-018-CLOUDFLARE-VLESS-WS-255MS` (url=511ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-223MS` (url=511ms, status=HTTP 204)
17. `AKUN-020-UNKNOWN-VLESS-WS-274MS` (url=594ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-268MS` (url=512ms, status=HTTP 204)
19. `AKUN-022-SPEEDTEST-VLESS-WS-271MS` (url=557ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-257MS` (url=517ms, status=HTTP 204)
21. `AKUN-028-UNKNOWN-VLESS-WS-512MS` (url=826ms, status=HTTP 204)
22. `AKUN-030-UNKNOWN-VLESS-WS-541MS` (url=1121ms, status=HTTP 204)
23. `AKUN-031-UNKNOWN-VLESS-WS-596MS` (url=989ms, status=HTTP 204)
24. `AKUN-032-UNKNOWN-VLESS-WS-670MS` (url=2429ms, status=HTTP 204)
25. `AKUN-035-UNKNOWN-VLESS-WS-539MS` (url=587ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
