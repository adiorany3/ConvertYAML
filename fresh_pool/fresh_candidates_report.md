# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
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
1. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-66MS` (url=217ms, nekobox=233ms, status=yes)
2. `AKUN-002-OPENAI-VLESS-WS-97MS` (url=224ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-97MS` (url=218ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-110MS` (url=217ms, nekobox=239ms, status=yes)
5. `AKUN-005-ALIBABA-VLESS-WS-102MS` (url=209ms, nekobox=242ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS` (url=198ms, nekobox=257ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-92MS` (url=220ms, nekobox=286ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-97MS` (url=238ms, nekobox=249ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-115MS` (url=220ms, nekobox=226ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS` (url=197ms, nekobox=182ms, status=no)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-250MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-254MS` (url=568ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-248MS` (url=487ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-244MS` (url=585ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-288MS` (url=556ms, status=HTTP 204)
16. `AKUN-021-UNKNOWN-VLESS-WS-234MS` (url=496ms, status=HTTP 204)
17. `AKUN-029-CLOUDFLARE-VLESS-WS-233MS` (url=485ms, status=HTTP 204)
18. `AKUN-032-UNKNOWN-VLESS-WS-621MS` (url=3511ms, status=HTTP 204)
19. `AKUN-033-UNKNOWN-VLESS-WS-487MS` (url=804ms, status=HTTP 204)
20. `AKUN-034-DEV-VLESS-WS-615MS` (url=710ms, status=HTTP 204)
21. `AKUN-035-UNKNOWN-VLESS-WS-548MS` (url=868ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
