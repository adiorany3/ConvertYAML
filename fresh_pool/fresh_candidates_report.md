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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-68MS` (url=205ms, nekobox=237ms, status=yes)
2. `AKUN-002-MYBB-VLESS-WS-82MS` (url=226ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=225ms, nekobox=194ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-90MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-79MS`
8. `AKUN-007-ADF-VLESS-WS-81MS`
9. `AKUN-008-UNKNOWN-VLESS-WS-165MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-99MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS`
12. `AKUN-013-CLOUDWEBMANAGE-EU-FR-VLESS-WS-74MS` (url=217ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-79MS` (url=203ms, status=HTTP 204)
14. `AKUN-015-DEV-VLESS-WS-221MS` (url=403ms, status=HTTP 204)
15. `AKUN-016-RS-RAPIDSEEDBOX-20190717-VLESS-WS-88MS` (url=203ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-80MS` (url=220ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-80MS` (url=226ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-240MS` (url=498ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-253MS` (url=561ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-76MS` (url=216ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-68MS` (url=221ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-239MS` (url=476ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-275MS` (url=545ms, status=HTTP 204)
24. `AKUN-025-US-VLESS-WS-70MS` (url=217ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-269MS` (url=549ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
