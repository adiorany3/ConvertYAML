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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-125MS` (url=263ms, nekobox=301ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-131MS` (url=259ms, nekobox=292ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-138MS` (url=273ms, nekobox=305ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-139MS` (url=266ms, nekobox=297ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-138MS` (url=265ms, nekobox=292ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-136MS` (url=262ms, nekobox=292ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-143MS` (url=369ms, nekobox=297ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-145MS` (url=267ms, nekobox=288ms, status=yes)
9. `AKUN-009-CLOUDWEBMANAGE-EU-FR-VLESS-WS-134MS` (url=262ms, nekobox=291ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-149MS` (url=295ms, nekobox=295ms, status=yes)
11. `AKUN-011-KIRINO-31-25-88-0-24-VLESS-WS-139MS` (url=259ms, status=HTTP 204)
12. `AKUN-012-VULTR-VLESS-WS-144MS` (url=270ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-147MS` (url=262ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-200MS` (url=264ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-148MS` (url=260ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-137MS` (url=267ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-283MS` (url=495ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-354MS` (url=725ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-355MS` (url=3189ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-377MS` (url=751ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-379MS` (url=747ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-377MS` (url=680ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-389MS` (url=747ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-382MS` (url=787ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-397MS` (url=797ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
