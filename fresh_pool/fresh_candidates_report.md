# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 19
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-UNKNOWN-VLESS-WS-134MS` (url=273ms, nekobox=293ms, status=yes)
2. `AKUN-002-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-135MS` (url=262ms, nekobox=301ms, status=yes)
3. `AKUN-003-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-143MS` (url=258ms, nekobox=297ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-172MS`
5. `AKUN-005-UNKNOWN-VLESS-WS-157MS`
6. `AKUN-007-CLOUDFLARE-VLESS-WS-156MS` (url=243ms, nekobox=231ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-142MS`
8. `AKUN-007-OPENAI-VLESS-WS-174MS`
9. `AKUN-010-CLOUDFLARE-VLESS-WS-163MS` (url=241ms, nekobox=231ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-157MS`
11. `AKUN-009-UNKNOWN-VLESS-WS-358MS`
12. `AKUN-010-MICROSOFT-VLESS-WS-377MS`
13. `AKUN-014-UNKNOWN-VLESS-WS-389MS` (url=2512ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-379MS` (url=736ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-361MS` (url=765ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-454MS` (url=805ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-417MS` (url=775ms, status=HTTP 204)
18. `AKUN-025-NET-77-93-90-0-VLESS-WS-267MS` (url=1620ms, status=HTTP 204)
19. `AKUN-034-DOGGOAPP-VLESS-WS-661MS` (url=1685ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
