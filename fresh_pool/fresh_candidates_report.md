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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=282ms, nekobox=318ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=325ms, nekobox=358ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-79MS` (url=307ms, nekobox=182ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS`
5. `AKUN-004-VULTR-VLESS-WS-74MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-89MS`
8. `AKUN-007-MEDIUM-VLESS-WS-78MS`
9. `AKUN-008-ADF-VLESS-WS-97MS`
10. `AKUN-009-MYBB-VLESS-WS-91MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS`
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-90MS` (url=267ms, status=HTTP 204)
13. `AKUN-013-DEV-VLESS-WS-187MS` (url=419ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-91MS` (url=284ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-77MS` (url=292ms, status=HTTP 204)
16. `AKUN-016-DIGITALOCEAN-VLESS-WS-110MS` (url=271ms, status=HTTP 204)
17. `AKUN-017-CLOUDWEBMANAGE-EU-FR-VLESS-WS-98MS` (url=290ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-76MS` (url=272ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-114MS` (url=269ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-263MS` (url=572ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-298MS` (url=655ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-79MS` (url=281ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-303MS` (url=650ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-321MS` (url=651ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-139MS` (url=303ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
