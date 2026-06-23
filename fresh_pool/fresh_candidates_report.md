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
1. `AKUN-001-UNKNOWN-VLESS-WS-134MS` (url=297ms, nekobox=298ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-141MS` (url=269ms, nekobox=219ms, status=no)
3. `AKUN-002-DIGITALOCEAN-VLESS-WS-144MS`
4. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-138MS`
5. `AKUN-006-CLOUDFLARE-VLESS-WS-145MS` (url=249ms, nekobox=236ms, status=no)
6. `AKUN-004-OPENAI-VLESS-WS-136MS`
7. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-140MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-146MS`
9. `AKUN-007-CLOUDFLARE-VLESS-WS-147MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-148MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-149MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-155MS`
13. `AKUN-014-UNKNOWN-VLESS-WS-170MS` (url=276ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-162MS` (url=248ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-177MS` (url=259ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-161MS` (url=273ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-143MS` (url=261ms, status=HTTP 204)
18. `AKUN-019-CLOUDWEBMANAGE-EU-FR-VLESS-WS-150MS` (url=272ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-139MS` (url=300ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-145MS` (url=278ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-345MS` (url=704ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-362MS` (url=701ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-384MS` (url=768ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-352MS` (url=671ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-391MS` (url=738ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
