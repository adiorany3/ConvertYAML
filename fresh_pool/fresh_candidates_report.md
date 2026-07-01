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
1. `AKUN-001-ALIBABA-VLESS-WS-73MS` (url=206ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-72MS` (url=221ms, nekobox=257ms, status=yes)
3. `AKUN-003-UK-GB-DCL-01-20191003-VLESS-WS-79MS` (url=224ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=230ms, nekobox=251ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=229ms, nekobox=182ms, status=no)
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-75MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS`
8. `AKUN-007-COMPREND-NET-VLESS-WS-107MS`
9. `AKUN-008-COMPREND-NET-VLESS-WS-105MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-69MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-98MS`
12. `AKUN-012-COMPREND-NET-VLESS-WS-112MS` (url=220ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-123MS` (url=279ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-133MS` (url=226ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-155MS` (url=249ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-78MS` (url=301ms, status=HTTP 204)
17. `AKUN-017-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=217ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-231MS` (url=519ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-242MS` (url=502ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-277MS` (url=580ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-110MS` (url=210ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-280MS` (url=605ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-265MS` (url=578ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-92MS` (url=218ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-260MS` (url=786ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
