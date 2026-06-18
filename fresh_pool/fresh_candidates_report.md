# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 17
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 23

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
1. `AKUN-001-MEDIUM-VLESS-WS-84MS` (url=218ms, nekobox=176ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-104MS`
3. `AKUN-003-SPEEDTEST-VLESS-WS-97MS` (url=199ms, nekobox=191ms, status=no)
4. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-77MS`
5. `AKUN-006-CLOUDFLARE-VLESS-WS-108MS` (url=206ms, nekobox=183ms, status=no)
6. `AKUN-003-CLOUDFLARE-VLESS-WS-108MS`
7. `AKUN-004-CLOUDFLARE-VLESS-WS-178MS`
8. `AKUN-005-CLOUDFLARE-VLESS-WS-227MS`
9. `AKUN-010-SPEEDTEST-VLESS-WS-107MS` (url=285ms, nekobox=581ms, status=no)
10. `AKUN-006-CLOUDFLARE-VLESS-WS-387MS`
11. `AKUN-007-WPENG-VLESS-WS-392MS`
12. `AKUN-008-CLOUDFLARE-VLESS-WS-389MS`
13. `AKUN-009-CONFLU-VLESS-WS-379MS`
14. `AKUN-026-SPEEDTEST-VLESS-WS-423MS` (url=3573ms, nekobox=514ms, status=no)
15. `AKUN-010-UNKNOWN-VLESS-WS-799MS`
16. `AKUN-033-DEV-VLESS-WS-223MS` (url=511ms, status=HTTP 204)
17. `AKUN-034-ONTHEWIFI-VLESS-WS-795MS` (url=1161ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
