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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=211ms, nekobox=235ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=211ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=229ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-86MS` (url=212ms, nekobox=238ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-71MS` (url=200ms, nekobox=234ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS` (url=218ms, nekobox=255ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-100MS` (url=228ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-69MS` (url=217ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-96MS` (url=223ms, nekobox=245ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-74MS` (url=209ms, nekobox=7177ms, status=no)
11. `AKUN-010-GO-DADDY-COM-LLC-VLESS-WS-92MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-97MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-NEXUSMODS-VLESS-WS-116MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-72MS` (url=212ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-81MS` (url=213ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-112MS` (url=221ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-116MS` (url=214ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-114MS` (url=217ms, status=HTTP 204)
19. `AKUN-019-PUBLICDOMAINREGISTRY-NET-VLESS-WS-102MS` (url=201ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-77MS` (url=224ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-115MS` (url=218ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-103MS` (url=232ms, status=HTTP 204)
23. `AKUN-023-ES-FORNEX-20160629-VLESS-WS-90MS` (url=205ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-89MS` (url=223ms, status=HTTP 204)
25. `AKUN-025-MEDIUM-VLESS-WS-117MS` (url=220ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
