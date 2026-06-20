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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-74MS` (url=217ms, nekobox=242ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-62MS` (url=211ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-85MS` (url=272ms, nekobox=262ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=206ms, nekobox=242ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=230ms, nekobox=226ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=217ms, nekobox=250ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-99MS` (url=216ms, nekobox=241ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-128MS` (url=232ms, nekobox=254ms, status=yes)
9. `AKUN-009-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-133MS` (url=207ms, nekobox=234ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-146MS` (url=219ms, nekobox=260ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-76MS` (url=211ms, status=HTTP 204)
12. `AKUN-012-RS-RAPIDSEEDBOX-20190717-VLESS-WS-129MS` (url=211ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-151MS` (url=229ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-151MS` (url=208ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-240MS` (url=503ms, status=HTTP 204)
16. `AKUN-017-WPENG-VLESS-WS-278MS` (url=587ms, status=HTTP 204)
17. `AKUN-018-CONFLU-VLESS-WS-236MS` (url=523ms, status=HTTP 204)
18. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-285MS` (url=602ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-256MS` (url=3664ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-270MS` (url=585ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-282MS` (url=580ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-376MS` (url=855ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-378MS` (url=578ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-428MS` (url=787ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-517MS` (url=851ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
