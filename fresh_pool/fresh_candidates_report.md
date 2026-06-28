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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-88MS` (url=260ms, nekobox=265ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-88MS` (url=224ms, nekobox=234ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-87MS` (url=233ms, nekobox=261ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS` (url=220ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDWEBMANAGE-EU-FR-VLESS-WS-95MS` (url=229ms, nekobox=232ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-95MS` (url=201ms, nekobox=240ms, status=yes)
7. `AKUN-007-DE-XTOM-20210903-VLESS-WS-77MS` (url=200ms, nekobox=240ms, status=yes)
8. `AKUN-008-VULTR-VLESS-WS-105MS` (url=224ms, nekobox=254ms, status=yes)
9. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-81MS` (url=219ms, nekobox=251ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-112MS` (url=200ms, nekobox=250ms, status=yes)
11. `AKUN-011-466688-VLESS-WS-100MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-92MS` (url=229ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-92MS` (url=208ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-130MS` (url=199ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-120MS` (url=239ms, status=HTTP 204)
17. `AKUN-017-US-VLESS-WS-102MS` (url=206ms, status=HTTP 204)
18. `AKUN-018-MEDIUM-VLESS-WS-86MS` (url=202ms, status=HTTP 204)
19. `AKUN-019-1PASSWORD-VLESS-WS-84MS` (url=226ms, status=HTTP 204)
20. `AKUN-020-MYBB-VLESS-WS-100MS` (url=210ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-240MS` (url=495ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-266MS` (url=603ms, status=HTTP 204)
23. `AKUN-023-MICROSOFT-VLESS-WS-275MS` (url=578ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-243MS` (url=504ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-245MS` (url=498ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
