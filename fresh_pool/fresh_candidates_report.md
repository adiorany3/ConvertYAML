# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-139MS` (url=261ms, nekobox=304ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-126MS` (url=256ms, nekobox=232ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-141MS`
4. `AKUN-003-OVH-VLESS-WS-135MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-137MS` (url=243ms, nekobox=226ms, status=no)
6. `AKUN-004-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-139MS`
7. `AKUN-005-LEVIKOGJGFDD-VLESS-WS-149MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-133MS`
9. `AKUN-007-UNKNOWN-VLESS-WS-152MS`
10. `AKUN-008-CLOUDFLARE-VLESS-WS-138MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-129MS` (url=246ms, nekobox=221ms, status=no)
12. `AKUN-009-CLOUDFLARE-VLESS-WS-134MS`
13. `AKUN-010-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-150MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-148MS` (url=285ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-153MS` (url=275ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-144MS` (url=271ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-235MS` (url=491ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-356MS` (url=730ms, status=HTTP 204)
19. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-363MS` (url=1076ms, status=HTTP 204)
20. `AKUN-025-SOSKEYNETS-VLESS-WS-511MS` (url=1150ms, status=HTTP 204)
21. `AKUN-026-CLOUDFLARE-VLESS-WS-574MS` (url=1067ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-623MS` (url=975ms, status=HTTP 204)
23. `AKUN-035-GAMEFICTOINSPEED-VLESS-WS-685MS` (url=1054ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
