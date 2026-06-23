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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-136MS` (url=262ms, nekobox=251ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-143MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-145MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-133MS`
5. `AKUN-004-DIGITALOCEAN-VLESS-WS-140MS`
6. `AKUN-005-1PASSWORD-VLESS-WS-140MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-137MS`
8. `AKUN-007-MEDIUM-VLESS-WS-147MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-155MS`
10. `AKUN-009-CLOUDWEBMANAGE-EU-FR-VLESS-WS-152MS`
11. `AKUN-010-ADF-VLESS-WS-141MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-157MS` (url=293ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-158MS` (url=384ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-150MS` (url=273ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-175MS` (url=330ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-168MS` (url=280ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-197MS` (url=246ms, status=HTTP 204)
18. `AKUN-019-RS-RAPIDSEEDBOX-20190717-VLESS-WS-201MS` (url=316ms, status=HTTP 204)
19. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-179MS` (url=287ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-145MS` (url=288ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-364MS` (url=744ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-370MS` (url=734ms, status=HTTP 204)
23. `AKUN-024-RS-RAPIDSEEDBOX-20190717-VLESS-WS-380MS` (url=736ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-390MS` (url=747ms, status=HTTP 204)
25. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-408MS` (url=780ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
