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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-103MS` (url=307ms, nekobox=276ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-113MS` (url=285ms, nekobox=279ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-106MS` (url=246ms, nekobox=318ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-129MS` (url=250ms, nekobox=275ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-129MS` (url=275ms, nekobox=276ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-138MS` (url=226ms, nekobox=322ms, status=yes)
7. `AKUN-007-OPENAI-VLESS-WS-133MS` (url=299ms, nekobox=280ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-158MS` (url=246ms, nekobox=225ms, status=no)
9. `AKUN-008-CLOUDFLARE-VLESS-WS-159MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-152MS` (url=270ms, nekobox=199ms, status=no)
11. `AKUN-009-CLOUDWEBMANAGE-EU-FR-VLESS-WS-136MS`
12. `AKUN-010-ADF-VLESS-WS-134MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-158MS` (url=283ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-160MS` (url=289ms, status=HTTP 204)
15. `AKUN-015-NET-NL-VLESS-WS-169MS` (url=234ms, status=HTTP 204)
16. `AKUN-016-U1HOST-FRA-VLESS-WS-129MS` (url=316ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-146MS` (url=247ms, status=HTTP 204)
18. `AKUN-018-SPACECORE-VLESS-WS-190MS` (url=278ms, status=HTTP 204)
19. `AKUN-019-DIGITALOCEAN-VLESS-WS-161MS` (url=292ms, status=HTTP 204)
20. `AKUN-020-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-142MS` (url=280ms, status=HTTP 204)
21. `AKUN-021-NETCUP-VLESS-WS-197MS` (url=284ms, status=HTTP 204)
22. `AKUN-022-CONFLU-VLESS-WS-291MS` (url=657ms, status=HTTP 204)
23. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-346MS` (url=733ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-354MS` (url=773ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-359MS` (url=773ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
