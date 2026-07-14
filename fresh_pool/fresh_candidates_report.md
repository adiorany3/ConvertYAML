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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-62MS` (url=213ms, nekobox=226ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=211ms, nekobox=230ms, status=yes)
3. `AKUN-003-1PASSWORD-VLESS-WS-76MS` (url=302ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-75MS` (url=217ms, nekobox=239ms, status=yes)
5. `AKUN-005-MYBB-VLESS-WS-77MS` (url=210ms, nekobox=243ms, status=yes)
6. `AKUN-006-NET-82-21-84-0-24-VLESS-WS-78MS` (url=197ms, nekobox=229ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-82MS` (url=236ms, nekobox=273ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-83MS` (url=200ms, nekobox=7177ms, status=no)
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-84MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-87MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS`
12. `AKUN-012-POLICE-VLESS-WS-96MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-88MS` (url=230ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-76MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-98MS` (url=202ms, status=HTTP 204)
16. `AKUN-016-ADF-VLESS-WS-81MS` (url=283ms, status=HTTP 204)
17. `AKUN-017-SHOPIFY-VLESS-WS-90MS` (url=305ms, status=HTTP 204)
18. `AKUN-018-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=225ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-115MS` (url=212ms, status=HTTP 204)
20. `AKUN-020-ES-FORNEX-20160629-VLESS-WS-137MS` (url=230ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-76MS` (url=236ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-132MS` (url=233ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-85MS` (url=197ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-101MS` (url=209ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-90MS` (url=224ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
