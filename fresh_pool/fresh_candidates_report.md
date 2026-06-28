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
1. `AKUN-001-VULTR-VLESS-WS-62MS` (url=218ms, nekobox=251ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-80MS` (url=230ms, nekobox=243ms, status=yes)
3. `AKUN-003-COMPREND-NET-VLESS-WS-100MS` (url=249ms, nekobox=257ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=239ms, nekobox=255ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=221ms, nekobox=258ms, status=yes)
6. `AKUN-006-COMPREND-NET-VLESS-WS-79MS` (url=312ms, nekobox=248ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-108MS` (url=205ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-116MS` (url=218ms, nekobox=260ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-70MS` (url=218ms, nekobox=192ms, status=no)
10. `AKUN-009-ZVC-VLESS-WS-138MS`
11. `AKUN-010-COMPREND-NET-VLESS-WS-113MS`
12. `AKUN-012-COMPREND-NET-VLESS-WS-104MS` (url=207ms, status=HTTP 204)
13. `AKUN-013-DE-CLOUDKLEYER-20220111-VLESS-WS-77MS` (url=229ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-115MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-99MS` (url=220ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-78MS` (url=217ms, status=HTTP 204)
17. `AKUN-017-SPEEDTEST-VLESS-WS-346MS` (url=811ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-361MS` (url=743ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-354MS` (url=730ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-370MS` (url=588ms, status=HTTP 204)
21. `AKUN-021-SPEEDTEST-VLESS-WS-398MS` (url=855ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-398MS` (url=856ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-447MS` (url=857ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-398MS` (url=913ms, status=HTTP 204)
25. `AKUN-029-RS-RAPIDSEEDBOX-20190717-VLESS-WS-727MS` (url=1174ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
