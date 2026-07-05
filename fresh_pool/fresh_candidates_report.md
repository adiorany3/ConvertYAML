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
1. `AKUN-001-NEXUSMODS-VLESS-WS-92MS` (url=233ms, nekobox=264ms, status=yes)
2. `AKUN-002-ZVC-VLESS-WS-89MS` (url=213ms, nekobox=235ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-94MS` (url=216ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-101MS` (url=234ms, nekobox=263ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-88MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-112MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-97MS`
9. `AKUN-009-WPENG-VLESS-WS-96MS`
10. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS`
11. `AKUN-012-WEYRO-NET-VLESS-WS-116MS` (url=228ms, status=HTTP 204)
12. `AKUN-013-WPENG-VLESS-WS-109MS` (url=215ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-111MS` (url=216ms, status=HTTP 204)
14. `AKUN-015-WPENG-VLESS-WS-119MS` (url=253ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-118MS` (url=288ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-330MS` (url=572ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-370MS` (url=781ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-309MS` (url=848ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-369MS` (url=761ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-398MS` (url=821ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-397MS` (url=843ms, status=HTTP 204)
22. `AKUN-024-SPEEDTEST-VLESS-WS-399MS` (url=773ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-400MS` (url=833ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-588MS` (url=1111ms, status=HTTP 204)
25. `AKUN-030-CLOUDFLARE-VLESS-WS-690MS` (url=1128ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
