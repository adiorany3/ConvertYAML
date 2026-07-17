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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=205ms, nekobox=352ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-77MS` (url=228ms, nekobox=253ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=228ms, nekobox=261ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-83MS` (url=220ms, nekobox=256ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS` (url=230ms, nekobox=243ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=209ms, nekobox=252ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=237ms, nekobox=241ms, status=yes)
8. `AKUN-008-466688-VLESS-WS-88MS` (url=204ms, nekobox=238ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-93MS` (url=210ms, nekobox=430ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-98MS` (url=222ms, nekobox=258ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-96MS` (url=204ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-93MS` (url=216ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=208ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-100MS` (url=201ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-105MS` (url=253ms, status=HTTP 204)
16. `AKUN-016-BGP48-HK-VLESS-WS-112MS` (url=215ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-90MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-109MS` (url=229ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-119MS` (url=233ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-140MS` (url=245ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-148MS` (url=277ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-88MS` (url=250ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-107MS` (url=295ms, status=HTTP 204)
24. `AKUN-024-POLICE-VLESS-WS-98MS` (url=248ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-171MS` (url=234ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
