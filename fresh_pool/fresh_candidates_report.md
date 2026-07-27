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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-83MS` (url=198ms, nekobox=231ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-87MS` (url=206ms, nekobox=236ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-83MS` (url=199ms, nekobox=229ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-84MS` (url=230ms, nekobox=228ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=199ms, nekobox=259ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-83MS` (url=198ms, nekobox=227ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=230ms, nekobox=240ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-94MS` (url=228ms, nekobox=243ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS` (url=199ms, nekobox=240ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=199ms, nekobox=259ms, status=yes)
11. `AKUN-011-SPEEDTEST-VLESS-WS-92MS` (url=209ms, status=HTTP 204)
12. `AKUN-012-SPEEDTEST-VLESS-WS-91MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=205ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-111MS` (url=217ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-95MS` (url=199ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-91MS` (url=198ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-125MS` (url=245ms, status=HTTP 204)
18. `AKUN-019-SPEEDTEST-VLESS-WS-106MS` (url=207ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-136MS` (url=261ms, status=HTTP 204)
20. `AKUN-022-SPEEDTEST-VLESS-WS-91MS` (url=230ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-101MS` (url=211ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-132MS` (url=289ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-366MS` (url=1206ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-364MS` (url=756ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-725MS` (url=1240ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
