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
1. `AKUN-001-VULTR-VLESS-WS-133MS` (url=291ms, nekobox=291ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-138MS` (url=249ms, nekobox=297ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-136MS` (url=281ms, nekobox=291ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-135MS` (url=243ms, nekobox=310ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-146MS` (url=305ms, nekobox=305ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-139MS` (url=245ms, nekobox=238ms, status=no)
7. `AKUN-006-CLOUDWEBMANAGE-EU-FR-VLESS-WS-142MS`
8. `AKUN-007-DIGITALOCEAN-VLESS-WS-157MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-146MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-154MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-165MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-156MS` (url=258ms, status=HTTP 204)
13. `AKUN-013-1PASSWORD-VLESS-WS-140MS` (url=245ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-148MS` (url=330ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-143MS` (url=284ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-150MS` (url=327ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-141MS` (url=268ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-137MS` (url=258ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-175MS` (url=288ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-293MS` (url=495ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-354MS` (url=712ms, status=HTTP 204)
22. `AKUN-022-OCTOPUSSS5-VLESS-WS-378MS` (url=742ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-393MS` (url=800ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-401MS` (url=753ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-394MS` (url=773ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
