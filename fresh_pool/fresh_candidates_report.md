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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=203ms, nekobox=230ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-66MS` (url=203ms, nekobox=240ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-90MS` (url=220ms, nekobox=238ms, status=yes)
4. `AKUN-004-DE-XTOM-20210903-VLESS-WS-89MS` (url=209ms, nekobox=254ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=210ms, nekobox=252ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-80MS` (url=218ms, nekobox=239ms, status=yes)
7. `AKUN-007-VULTR-VLESS-WS-73MS` (url=205ms, nekobox=235ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=224ms, nekobox=231ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-86MS` (url=211ms, nekobox=250ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-85MS` (url=231ms, nekobox=241ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-73MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-84MS` (url=199ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-105MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-85MS` (url=201ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-127MS` (url=216ms, status=HTTP 204)
16. `AKUN-016-COMPREND-NET-VLESS-WS-99MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-CLOUDWEBMANAGE-EU-FR-VLESS-WS-118MS` (url=235ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-70MS` (url=218ms, status=HTTP 204)
19. `AKUN-019-US-VLESS-WS-113MS` (url=211ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-110MS` (url=213ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-245MS` (url=482ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-254MS` (url=605ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-257MS` (url=543ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-254MS` (url=595ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-271MS` (url=652ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
